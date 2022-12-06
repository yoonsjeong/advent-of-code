/* Returns 1 for win, -1 for loss, 0 for tie. */
var rpsSimulator = (opp, me) => {
    if (opp == me) return 0;
    if (opp == "r" && me == "p") return 1;
    if (opp == "p" && me == "s") return 1;
    if (opp == "s" && me == "r") return 1;
    else return -(rpsSimulator(me, opp));
}

var scoreNormalizer = (result) => {
    if (result == 1) return 6;
    if (result == 0) return 3;
    if (result == -1) return 0;
}

var scorePlay = (play) => {
    if (play == "r") return 1;
    if (play == "p") return 2;
    if (play == "s") return 3;
}

var gameTranslator = (opp, me) => {
    let oppDict = { A: "r", B: "p", C: "s" };
    let meDict = { X: "r", Y: "p", Z: "s" };
    return [oppDict[opp], meDict[me]];
}

var rpsSimulatorBackwards = (opp, result) => {
    let winDict = { r: "p", p: "s", s: "r" };
    let loseDict = { p: "r", s: "p", r: "s" };
    if (result == 1) return winDict[opp];
    if (result == 0) return opp;
    if (result == -1) return loseDict[opp];
}

var gameTranslatorPart2 = (opp, me) => {
    let oppDict = { A: "r", B: "p", C: "s" }
    let meDict = { X: -1, Y: 0, Z: 1 }
    return [oppDict[opp], meDict[me]];
    
    
}

var part1 = (gameList) => {
    let totalScore = 0;
    for (let game of gameList) {
        let [opp, me] = gameTranslator(...game.split(" "));
        let score = scoreNormalizer(rpsSimulator(opp, me)) + scorePlay(me);
        totalScore += score;
    }
    return totalScore;
}

var part2 = (gameList) => {
    let totalScore = 0;
    for (let game of gameList) {
        let [opp, me] = gameTranslatorPart2(...game.split(" "));
        let score = scoreNormalizer(me) + scorePlay(rpsSimulatorBackwards(opp, me))
        totalScore += score;
    }
    return totalScore;
}

var main = (input) => {
    let gameList = input.split("\r\n");

    let p1 = part1(gameList);
    let p2 = part2(gameList);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-02.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
