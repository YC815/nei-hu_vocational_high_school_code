for (let y = 0; y < 18; y++) { // 這裡的 18 代表條數
    for (let x = 0; x < countX; x++) {
        board[x + y * countX] = 0; // 使用顏色索引 0 填滿每一行
    }
}