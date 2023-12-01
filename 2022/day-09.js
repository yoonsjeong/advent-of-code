var moveInDirection = (direction, count, positionsSet) => {

}

var part1 = () => {
    let head_coord = `0,0`
    let tail_coord = `0,0`
    

    const positionsSet = set = new Set()
    for (const movement of object) {
        
    }
    let [head_x, head_y] = head_coord.split(",")
    let [tail_x, tail_y] = tail_coord.split(",")
    
    let [x_dist, y_dist] = [(+tail_x) - (+head_x), (+tail_y) - (+head_y)]
    let dist = Math.abs(x_dist) + Math.abs(y_dist);

    /* if diagonal */
    if (dist > 2 || Math.abs(x_dist) == 1 && Math.abs(y_dist) == 1) continue;
    else {

    }
}

var part2 = () => {
}

var main = (input) => {
    let logicalMapOfTrees = convertToLogical(input);
    let p1 = part1();
    let p2 = part2();

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-08.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
