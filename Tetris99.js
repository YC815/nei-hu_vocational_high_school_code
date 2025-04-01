function fillLine(y) {
    if (y > 20) return;
    for (let x = 0; x < 40; x++) {
        board[x + y * 40] = 0;
    }
    down()
    check()
    setTimeout(() => fillLine(y + 1), 1);
}
fillLine(0);
