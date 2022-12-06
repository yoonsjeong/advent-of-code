var getElfCargoCalorieArray = (elfCargoStringArray) => {
    let elfCargoCalorieArray = elfCargoStringArray.map(elfCargoString => {
        let cargoCalorieArray = elfCargoString.split("\r\n");
        let sumCalorie = cargoCalorieArray
            .map(calorieString => parseInt(calorieString))
            .reduce((a, b) => a + b);
        return sumCalorie;
    })
    return elfCargoCalorieArray;
}

var part1 = (elfCargoStringArray) => {
    let elfCargoCalorieArray = getElfCargoCalorieArray(elfCargoStringArray);
    return Math.max(...elfCargoCalorieArray);
}

var part2 = (elfCargoStringArray) => {
    let cargoCalorieArray = getElfCargoCalorieArray(elfCargoStringArray);
    console.log(cargoCalorieArray);
    let topThree = [0, 0, 0];
    for (let calorieSum of cargoCalorieArray)
    {
        if (calorieSum > topThree[0])
        {
            topThree[1] = topThree[0]
            topThree[2] = topThree[1]
            topThree[0] = calorieSum
        }
        else if (calorieSum > topThree[1])
        {
            topThree[2] = topThree[1];
            topThree[1] = calorieSum;
        }
        else if (calorieSum > topThree[2])
        {
            topThree[2] = calorieSum;
        }
    }
    console.log("topthree", topThree);
    return topThree.reduce((a, b) => a + b);
}

// input: string
var main = (input) => {
    // string[]
    let elfCargoStringArray = input.split("\r\n\r\n");
    // 
    let p1 = part1(elfCargoStringArray);
    let p2 = part2(elfCargoStringArray);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-01.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
