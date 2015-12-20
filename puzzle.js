function optimize (T, S) {
    var delta = 0,
    pair = null,
    total = 0;
    function compare (x) {
        var y = T[x] + T[x+1] - S[x];
        if (y > delta) {
            delta = y;
            pair = x;
        }
    };
    for (var i = 0, len = S.length; i < len; i++) {
        compare(i);
    };
    for (var j = 0, len = T.length; j < len; j++) {
        if (j === pair) {
            total += S[j];
        } else if (j === (pair + 1)) {
            //skip
        } else {
            total += T[j];
        }
    }
    return total;
}
