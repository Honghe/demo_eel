<!--   Disable F5 key     -->
window.onload = function () {
    document.onkeydown = function (e) {
        return (e.which || e.keyCode) !== 116;
    };
};

// https://github.com/ChrisKnott/Eel/issues/86
async function getFolder() {
    var dosya_path = await eel.btn_get_folder()();
    if (dosya_path) {
        console.log(dosya_path);
    }
}

async function getFile() {
    var filepath = await eel.btn_get_file()();
    if (filepath) {
        console.log(filepath);
    }
}