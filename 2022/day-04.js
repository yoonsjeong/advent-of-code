var part1 = (pairList) => {
    let reassignments = 0;
    for (let pair of pairList)
    {
        let [pair1, pair2] = pair.split(",");
        let [pair1_1, pair1_2] = pair1.split("-").map(v => parseInt(v));
        let [pair2_1, pair2_2] = pair2.split("-").map(v => parseInt(v));
        
        /* pair1 inside pair2 */
        if ((pair2_1 <= pair1_1) && (pair1_2 <= pair2_2))
            reassignments++;
        /* pair2 inside pair1 */
        else if ((pair1_1 <= pair2_1) && (pair2_2 <= pair1_2))
            reassignments++;
    }
    return reassignments;
}

var part2 = (pairList) => {
    let reassignments = 0;
    for (let pair of pairList)
    {
        let [pair1, pair2] = pair.split(",");
        let [pair1_1, pair1_2] = pair1.split("-").map(v => parseInt(v));
        let [pair2_1, pair2_2] = pair2.split("-").map(v => parseInt(v));
        
        /* part of pair1 intrudes pair2 */
        if ((pair2_1 <= pair1_1) && (pair1_1 <= pair2_2))
            reassignments++;
        /* part of pair2 intrudes pair1 */
        else if ((pair1_1 <= pair2_1) && (pair2_1 <= pair1_2))
            reassignments++;
    }
    return reassignments;
}

var main = (input) => {
    let pairList = input.split("\r\n");

    let p1 = part1(pairList);
    let p2 = part2(pairList);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-04.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
