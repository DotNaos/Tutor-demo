import streamlit as st
import json
import ast
from streamlit_ace import st_ace

# Funktion zum Laden des Favicon als Bytes
def get_favicon():
    try:
        with open("favicon.ico", "rb") as f:
            favicon_bytes = f.read()
        return favicon_bytes
    except FileNotFoundError:
        st.warning("Favicon nicht gefunden. Bitte stellen Sie sicher, dass 'favicon.ico' im selben Verzeichnis ist.")
        return None

# Favicon laden
favicon = get_favicon()

# Seite konfigurieren mit Favicon
st.set_page_config(
    page_title="FHGR Tutor-App",
    layout="wide",
    page_icon=favicon if favicon else "🖥️"  # Fallback zu einem Emoji, falls Favicon fehlt
)

st.title("FHGR Tutor-App")

# Funktion zum Laden der Aufgaben aus der JSON-Datei
def load_aufgaben(datei_pfad):
    try:
        with open(datei_pfad, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Datei '{datei_pfad}' nicht gefunden.")
        return []
    except json.JSONDecodeError as e:
        st.error(f"Fehler beim Parsen der JSON-Datei: {e}")
        return []

# Aufgaben laden
aufgaben = load_aufgaben("aufgaben.json")

# Navigationsreiter mit "String-Methoden"
tabs = st.tabs(["String-Methoden"])
# Weitere Reiter können hier in der Liste hinzugefügt werden, z.B. "Listen", "Dictionaries", etc.

with tabs[0]:
    st.header("String-Methoden")

    # Anzeige der Aufgaben
    for aufgabe in aufgaben:
        st.markdown(f"### Aufgabe {aufgabe['id']}: {aufgabe['titel']}")
        st.markdown(f"<p>{aufgabe['beschreibung']}</p>", unsafe_allow_html=True)

        # Vorbereiten des Code-Inputs mit vorgefertigtem Funktionskopf
        code_vorlage = aufgabe["funktion"]

        # Syntax-Highlighting mit streamlit-ace und einem vorhandenen Theme
        user_code = st_ace(
            value=code_vorlage,
            language='python',
            theme='catpuccin',  # Verwenden eines vorhandenen Themes wie 'dracula'
            key=f"code_{aufgabe['id']}",
            font_size=14,
            show_gutter=True,
            show_print_margin=True,
            wrap=True,
            auto_update=True,
            tab_size=4,
            keybinding='vscode',  # Ähnlich wie VSCode
        )

        # Button zum Testen des Codes
        if st.button("Testen", key=f"button_{aufgabe['id']}"):
            if not user_code or user_code.strip() == aufgabe["funktion"].strip():
                st.error("Bitte vervollständigen Sie Ihre Funktion, bevor Sie sie testen.")
            else:
                # Bereich für die Testergebnisse
                with st.expander("Testergebnisse", expanded=True):
                    try:
                        # Lokaler Namespace für die Ausführung des Codes
                        local_namespace = {}
                        exec(user_code, {}, local_namespace)

                        # Extrahieren des Funktionsnamens aus dem gesamten Benutzercode
                        try:
                            parsed_code = ast.parse(user_code)
                            func_name = None
                            for node in parsed_code.body:
                                if isinstance(node, ast.FunctionDef):
                                    func_name = node.name
                                    break
                            if not func_name:
                                st.error("Die Funktion wurde nicht korrekt definiert.")
                            else:
                                user_func = local_namespace.get(func_name)

                                if not callable(user_func):
                                    st.error("Die definierte Funktion ist nicht aufrufbar.")
                                else:
                                    alle_bestanden = True
                                    st.markdown("#### Testergebnisse:")
                                    for idx, test in enumerate(aufgabe["test_cases"], 1):
                                        input_args = test["input"]
                                        erwartetes = test["output"]
                                        try:
                                            ergebnis = user_func(*input_args)
                                            if ergebnis != erwartetes:
                                                st.error(
                                                    f"**Testfall {idx} fehlgeschlagen:**\n"
                                                    f"Eingabe: `{input_args}`\n"
                                                    f"Erwartet: `{erwartetes}`, erhalten: `{ergebnis}`."
                                                )
                                                alle_bestanden = False
                                            else:
                                                st.success(
                                                    f"**Testfall {idx} bestanden:** Eingabe `{input_args}` ergibt `{ergebnis}`."
                                                )
                                        except Exception as e:
                                            st.error(
                                                f"**Fehler bei Testfall {idx} mit Eingabe `{input_args}`:** {e}"
                                            )
                                            alle_bestanden = False

                                    if alle_bestanden:
                                        st.balloons()
                                        st.success("Alle Tests bestanden! 🎉")
                        except SyntaxError as se:
                            st.error(f"Syntaxfehler im Code: {se}")
                        except Exception as e:
                            st.error(f"Fehler beim Parsen des Codes: {e}")

                    except Exception as e:
                        st.error(f"Fehler beim Ausführen des Codes: {e}")

        st.markdown("---")
