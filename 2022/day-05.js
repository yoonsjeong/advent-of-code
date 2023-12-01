var convertInstructionToLogical = (instruction) => {
    let [_, quantity,
        source,
        destination
    ] = instruction.match(/move (\d+) from (\d+) to (\d+)/);

    return {
        quantity: parseInt(quantity),
        source: parseInt(source) - 1,
        destination: parseInt(destination) - 1
    }
}

var convertBoardToLogical = (board) => {
    const [lastRow] = board.split("\r\n").slice(-1);
    const [lastNumber] = lastRow.trim().split(" ").slice(-1);
    const numberOfStacks = parseInt(lastNumber);

    let gameBoard = [...Array(numberOfStacks)].map(() => Array());
    for (let row of board.split("\r\n").slice(0, -1).reverse())
    {
        for (let k = 0; k < numberOfStacks; k++)
        {
            const letter = row[(4 * k) + 1];
            if (letter == " ") continue;
            gameBoard[k].push(letter);
        }
    }

    return gameBoard;
}

var executeCommand = (board, instruction) => {
    const { quantity, source, destination } = instruction;
    for (let i = 0; i < quantity; i++)
    {
        const poppedItem = board[source].pop();
        board[destination].push(poppedItem);
    }
}

var getMessageFromBoard = (board) => {
    let answer = "";
    for (let stack of board)
    {
        let [ topCrate ] = stack.slice(-1);
        answer += topCrate;
    }

    return answer;
}

var executeCommandPart2 = (board, instruction) => {
    const { quantity, source, destination } = instruction;
    let poppedItems = board[source].slice(-quantity);
    let leftoverItems = board[source].slice(0, -quantity);
    let newDestBoard = board[destination].concat(poppedItems);
    board[source] = leftoverItems;
    board[destination] = newDestBoard;
}

var part1 = (startingBoard, instructionList) => {
    let logicalInstructions = instructionList.split("\r\n").map(convertInstructionToLogical)
    const board = convertBoardToLogical(startingBoard);

    for (let instruction of logicalInstructions)
    {
        executeCommand(board, instruction);
    }

    return getMessageFromBoard(board);
}

var part2 = (startingBoard, instructionList) => {
    let logicalInstructions = instructionList.split("\r\n").map(convertInstructionToLogical)
    const board = convertBoardToLogical(startingBoard);

    for (let instruction of logicalInstructions)
    {
        executeCommandPart2(board, instruction);
    }

    return getMessageFromBoard(board);
}

var main = (input) => {
    let [startingBoard, instructionList] = input.split("\r\n\r\n");


    let p1 = part1(startingBoard, instructionList);
    let p2 = part2(startingBoard, instructionList);

    console.log(`The answer to part 1 is: ${p1}`);
    console.log(`The answer to part 2 is: ${p2}`);
}

/* parse and enter */
require("fs").readFile("day-05.txt", "utf8", (err, data) => {
    err && console.error(err);
    main(data);
})
