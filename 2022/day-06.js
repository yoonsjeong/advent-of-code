var allUniqueChars = (chars) => {
    return chars.length == (new Set(chars)).size;
}

var readWindow = (buffer, windowSize, startAt) => {
    return buffer
        .split("")
        .slice(startAt, startAt + windowSize)
        .join("");
}

var part1 = (buffer, windowSize) => {
    let result;
    for (let i = 0; i < buffer.length - windowSize; i++)
    {
        result = i + windowSize;
        if (allUniqueChars(readWindow(buffer, windowSize, i)))
            break;
    }
    return result;
}

var part2 = () => {
}

var main = (input) => {
    let p1 = part1(input, 4);
    let p2 = part1(input, 14);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-06.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
