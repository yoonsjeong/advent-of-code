var createEmptyArray = (n, m) => {
    return Array.from(Array(m), () => Array(n))
}

var convertToLogical = (input) => {
    const rows = input.split("\r\n");
    const [width, height] = [rows[0].length, rows.length]
    const logicalArray = createEmptyArray(width, height);

    for (let i = 0; i < width; i++) {
        for (let j = 0; j < height; j++) {
            let tree = rows[i][j];
            logicalArray[i][j] = parseInt(tree);
        }
    }
    return logicalArray;
}

var isVisible = (logicalMapOfTrees, i, j) => {
    const [width, height] = [logicalMapOfTrees[0].length, logicalMapOfTrees.length]
    let actual = logicalMapOfTrees[i][j]
    /* look north */
    let [north_dir, south_dir, east_dir, west_dir] = [true, true, true, true];
    for (let new_i = i + 1; new_i < width; new_i++)
        if (logicalMapOfTrees[new_i][j] >= actual)
            north_dir = false;
    /* look south */
    for (let new_i = i - 1; new_i >= 0; new_i--)
        if (logicalMapOfTrees[new_i][j] >= actual)
            south_dir = false;
    /* look east */
    for (let new_j = j + 1; new_j < height; new_j++)
        if (logicalMapOfTrees[i][new_j] >= actual)
            east_dir = false;
    /* look west */
    for (let new_j = j - 1; new_j >= 0; new_j--)
        if (logicalMapOfTrees[i][new_j] >= actual)
            west_dir = false;
    return north_dir || south_dir || east_dir || west_dir;
}

var getScenicScore = (logicalMapOfTrees, i, j) => {
    const [width, height] = [logicalMapOfTrees[0].length, logicalMapOfTrees.length]
    let actual = logicalMapOfTrees[i][j]
    /* look north */
    let [north_dir, south_dir, east_dir, west_dir] = [0, 0, 0, 0];
    for (let new_i = i + 1; new_i < width; new_i++) {
        if (logicalMapOfTrees[new_i][j] >= actual) {
            north_dir++;
            break;
        }
        north_dir++;
    }
    /* look south */
    for (let new_i = i - 1; new_i >= 0; new_i--) {
        if (logicalMapOfTrees[new_i][j] >= actual) {
            south_dir++;
            break;
        }
        south_dir++;
    }
    /* look east */
    for (let new_j = j + 1; new_j < height; new_j++) {
        if (logicalMapOfTrees[i][new_j] >= actual) {
            east_dir++;
            break;
        }
        east_dir++;
    }
    /* look west */
    for (let new_j = j - 1; new_j >= 0; new_j--) {
        if (logicalMapOfTrees[i][new_j] >= actual) {
            west_dir++;
            break;
        }
        west_dir++;
    }
    return north_dir * south_dir * east_dir * west_dir;
}

var part1 = (logicalMapOfTrees) => {
    const [width, height] = [logicalMapOfTrees[0].length, logicalMapOfTrees.length]

    let counter = 0;
    for (let i = 0; i < width; i++) {
        for (let j = 0; j < height; j++) {
            /* ignore outer rims */
            if (i == 0 || j == 0 || i == width || j == height) counter++;
            else if (isVisible(logicalMapOfTrees, i, j)) counter++;
        }        
    }

    return counter;
}

var part2 = (logicalMapOfTrees) => {    
    const [width, height] = [logicalMapOfTrees[0].length, logicalMapOfTrees.length]

    let highestScenicScore = 0;
    for (let i = 0; i < width; i++) {
        for (let j = 0; j < height; j++) {
            let currScore = getScenicScore(logicalMapOfTrees, i, j);
            if (currScore > highestScenicScore)
                highestScenicScore = currScore//, console.log("i, j", i, j, currScore);
        }        
    }

    return highestScenicScore;
}

var main = (input) => {
    let logicalMapOfTrees = convertToLogical(input);
    let p1 = part1(logicalMapOfTrees);
    let p2 = part2(logicalMapOfTrees);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-08.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
