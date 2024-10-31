line = 0;
$("#line").text(line);
function fillLine(y) {
    for (let x = 0; x < countX; x++) {
        board[x + y * countX] = 0;
    }
    line++;
    $("#line").text(line);
    check();

    if (line >= 18) return;

    setTimeout(() => fillLine(y + 1), 500);
}

fillLine(10);
