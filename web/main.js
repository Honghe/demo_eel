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
        selected_file = document.getElementById('selected_file');
        selected_file.value = filepath;
    }
}

async function process_file() {
    let selected_file = document.getElementById('selected_file').value;
    let prologue = document.getElementById('prologue').value;
    let epilogue = document.getElementById('epilogue').value;

    await display_loader(true);
    let ret = await eel.process_file(selected_file, prologue, epilogue)();
    await process_file_finish(ret);
}

async function display_loader(display) {
    let loader = document.getElementById('loader');
    let loader_end = document.getElementById('loader_end');
    if (display) {
        loader.style.display = "unset";
        loader_end.style.display = "none";
    } else {
        loader.style.display = "none";
    }
}


async function process_file_finish(msg) {
    console.log(process_file_finish);
    await display_loader(false);
    let loader_end = document.getElementById('loader_end');
    loader_end.style.display = "unset";
    loader_end.innerText = msg;
}