var findRepeatingLetter = (firstCompart, secondCompart) => {
    let firstSet = new Set(firstCompart);
    let secondSet = new Set(secondCompart);
    for (let item of firstSet)
    {
        if (secondSet.has(item)) return item;
    }
}

var getPriority = (item) => {
    let asciiNumber = item.charCodeAt();
    if (96 <= asciiNumber && asciiNumber <= 122)
        return asciiNumber - 96;
    else
        return asciiNumber - 38;
}

var findRepeatingLetterPart2 = (first, second, third) => {
    let firstSet = new Set(first);
    let secondSet = new Set(second);
    let thirdSet = new Set(third);

    let firstSecondRepeats = new Set();
    for (let item of firstSet)
        if (secondSet.has(item)) firstSecondRepeats.add(item);
    for (let repeat of firstSecondRepeats)
        if (thirdSet.has(repeat)) return repeat;
}

var part1 = (rucksackList) => {
    let totalSum = 0;
    for (let rucksack of rucksackList)
    {
        let halfMark = rucksack.length / 2;
        let compartments = [
            rucksack.slice(0, halfMark), 
            rucksack.slice(halfMark)
        ];
        totalSum += getPriority(findRepeatingLetter(...compartments));
    }
    return totalSum;
}

var part2 = (rucksackList) => {
    let totalSum = 0;
    for (let i = 0; i < rucksackList.length; i += 3)
    {
        let group = [
            rucksackList[i],
            rucksackList[i + 1],
            rucksackList[i + 2]
        ]
        totalSum += getPriority(findRepeatingLetterPart2(...group))
    }
    return totalSum;
}

var main = (input) => {
    let rucksackList = input.split("\r\n");

    let p1 = part1(rucksackList);
    let p2 = part2(rucksackList);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-03.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
