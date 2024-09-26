ace.define("ace/theme/catpuccin",["require","exports","module","ace/lib/dom"], function(require, exports, module) {
    exports.isDark = true;
    exports.cssClass = "ace-catpuccin";
    exports.cssText = `
.ace-catpuccin .ace_gutter {
    background: #1e1e2e;
    color: #c0caf5
}
.ace-catpuccin .ace_print-margin {
    width: 1px;
    background: #282a36
}
.ace-catpuccin {
    background-color: #1e1e2e;
    color: #c0caf5
}
.ace-catpuccin .ace_cursor {
    color: #c0caf5
}
.ace-catpuccin .ace_marker-layer .ace_selection {
    background: #44475a
}
.ace-catpuccin.ace_multiselect .ace_selection.ace_start {
    box-shadow: 0 0 3px 0px #1e1e2e;
    border-radius: 2px
}
.ace-catpuccin .ace_marker-layer .ace_step {
    background: rgb(102, 82, 0)
}
.ace-catpuccin .ace_marker-layer .ace_bracket {
    margin: -1px 0 0 -1px;
    border: 1px solid #c0caf5
}
.ace-catpuccin .ace_marker-layer .ace_active-line {
    background: #282a36
}
.ace-catpuccin .ace_gutter-active-line {
    background-color: #282a36
}
.ace-catpuccin .ace_marker-layer .ace_selected-word {
    border: 1px solid #44475a
}
.ace-catpuccin .ace_invisible {
    color: #3b4261
}
.ace-catpuccin .ace_keyword,
.ace-catpuccin .ace_meta,
.ace-catpuccin .ace_storage,
.ace-catpuccin .ace_storage.ace_type,
.ace-catpuccin .ace_support.ace_type {
    color: #f7768e
}
.ace-catpuccin .ace_keyword.ace_operator {
    color: #f7768e
}
.ace-catpuccin .ace_constant.ace_character,
.ace-catpuccin .ace_constant.ace_language,
.ace-catpuccin .ace_constant.ace_numeric,
.ace-catpuccin .ace_keyword.ace_other.ace_unit {
    color: #9ece6a
}
.ace-catpuccin .ace_constant.ace_other {
    color: #c0caf5
}
.ace-catpuccin .ace_invalid {
    color: #1e1e2e;
    background-color: #f7768e
}
.ace-catpuccin .ace_invalid.ace_deprecated {
    color: #1e1e2e;
    background-color: #f7768e
}
.ace-catpuccin .ace_fold {
    background-color: #e0af68;
    border-color: #c0caf5
}
.ace-catpuccin .ace_support.ace_function {
    color: #e0af68
}
.ace-catpuccin .ace_string {
    color: #9ece6a
}
.ace-catpuccin .ace_comment {
    color: #7aa2f7
}
.ace-catpuccin .ace_variable {
    color: #9ece6a
}
.ace-catpuccin .ace_meta.ace_tag {
    color: #7aa2f7
}
.ace-catpuccin .ace_entity.ace_other.ace_attribute-name {
    color: #e0af68
}
.ace-catpuccin .ace_entity.ace_name.ace_function {
    color: #e0af68
}
`;

    var dom = require("../lib/dom");
    dom.importCssString(exports.cssText, exports.cssClass);
});
