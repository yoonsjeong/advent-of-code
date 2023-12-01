class Valve {
  constructor(name, flow) {
    this.name = name;
    this.flow = parseInt(flow);
    this.connections = [];
  }

  addConnection(valve) {
    this.connections.push(valve);
  }
}

var getExplorationOfValves = (valve, time) => {
  Array(time)
}

var part1 = () => {

};

var part2 = () => {};

var parseInput = (input) => {
  let valveNameToValve = {};
  let valveNameToRawConnections = {};

  const regex =
    /Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w+,? ]+)/;

  for (const line of input.split("\r\n")) {
    const [_, valve, flow, rawConnections] = line.match(regex);
    valveNameToValve[valve] = new Valve(valve, flow);
    valveNameToRawConnections[valve] = rawConnections.split(", ");
  }

  for (const valve in valveNameToRawConnections) {
    for (const connect of valveNameToRawConnections[valve]) {
      let valveToConnect = valveNameToValve[connect];
      valveNameToValve[valve].addConnection(valveToConnect);
    }
  }
  return valveNameToValve;
};

var main = (input) => {
  let valveDictionary = parseInput(input);
  let p1 = part1(valveDictionary);
  let p2 = part2();

  console.log(`The answer to part 1 is: ${p1}`);
  console.log(`The answer to part 2 is: ${p2}`);
};

/* parse and enter */
require("fs").readFile("day-16.txt", "utf8", (err, data) => {
  err && console.error(err);
  main(data);
});
