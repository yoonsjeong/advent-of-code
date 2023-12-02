using System.Collections;
using System.Text.RegularExpressions;

int RED_MAX = 12;
int GREEN_MAX = 13;
int BLUE_MAX = 14;
string testInput = @"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
int part1Result = Part1(testInput);
Console.WriteLine($"Part 1 result: {part1Result}");
int part2Result = Part2(testInput);
Console.WriteLine($"Part 2 result: {part2Result}");

int Part1(string input)
{
    var lines = input.Split("\r\n");
    Regex gamePattern = new Regex(@"Game (\d+): (.+)");

    List<int> goodGames = new List<int>();
    foreach (var line in lines)
    {
        var captures = gamePattern.Match(line).Groups;
        int gameRound = int.Parse(captures[1].Value);
        string entireGame = captures[2].Value;

        var allSets = entireGame.Split(";");

        bool goodGame = true;
        foreach (string set in allSets)
        {
            if (ParseGameSetString(set).red > RED_MAX ||
                ParseGameSetString(set).green > GREEN_MAX ||
                ParseGameSetString(set).blue > BLUE_MAX)
            {
                goodGame = false;
            }
        }

        if (goodGame)
        {
            goodGames.Add(gameRound);
        }
    }

    int result = goodGames.Aggregate((a, b) => a + b);
    return result;
}

/* 3 blue, 4 green => red=0, blue=3, green=4*/
GameSet ParseGameSetString(string gameSet)
{
    var pulls = gameSet.Split(",");
    Regex pattern = new Regex(@"(\d+) (red|green|blue)");
    GameSet result = new GameSet();
    foreach (var pull in pulls)
    {
        var captures = pattern.Match(pull).Groups;
        int number = int.Parse(captures[1].Value);
        string color = captures[2].Value;
        switch (color)
        {
            case "red":
                result.red = number;
                break;
            case "green":
                result.green = number;
                break;
            case "blue":
                result.blue = number;
                break;
            default:
                break;
        }
    }
    return result;
}

int Part2(string input)
{
    var lines = input.Split("\r\n");
    Regex gamePattern = new Regex(@"Game (\d+): (.+)");

    List<int> powers = new List<int>();
    foreach (var line in lines)
    {
        var captures = gamePattern.Match(line).Groups;
        int gameRound = int.Parse(captures[1].Value);
        string entireGame = captures[2].Value;

        var allSets = entireGame.Split(";");

        int redMin = 0, greenMin = 0, blueMin = 0;
        foreach (string set in allSets)
        {
            var parsedSet = ParseGameSetString(set);
            redMin = parsedSet.red > redMin ? parsedSet.red : redMin; 
            greenMin = parsedSet.green > greenMin ? parsedSet.green : greenMin; 
            blueMin = parsedSet.blue > blueMin ? parsedSet.blue : blueMin; 
        }

        int power = redMin * greenMin * blueMin;
        powers.Add(power);
    }

    int result = powers.Aggregate((a, b) => a + b);
    return result;
}

struct GameSet
{
    public int red;
    public int blue;
    public int green;
}

