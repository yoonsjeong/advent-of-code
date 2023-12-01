using System;
using System.Linq;
using System.Text.RegularExpressions;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{
		string testEntry1 = @"1abc2
			pqr3stu8vwx
			a1b2c3d4e5f
			treb7uchet";
		Console.WriteLine("part 1");
		Part1(testEntry1);
		
		string testEntry2 = @"two1nine
			eightwothree
			abcone2threexyz
			xtwone3four
			4nineeightseven2
			zoneight234
			7pqrstsixteen";
		Console.WriteLine("part 2");
		Part2(testEntry2);
	}

	public static void Part1(string fullEntries)
	{
		List<string> entries = fullEntries.Split('\n').ToList();
		Regex firstDigitPattern = new Regex(@"^[^\d]*(\d)");
		Regex lastDigitPattern = new Regex(@"(\d)[^\d]*$");
 
		List<int> numbers = new List<int>();
		foreach (var entry in entries)
		{
			string first = firstDigitPattern.Match(entry).Groups[1].Value;
			string last = lastDigitPattern.Match(entry).Groups[1].Value;
			int result = int.Parse(first + last);
			numbers.Add(result);
		}
		
		int finalResult = numbers.Aggregate((a, b) => a + b);
		Console.WriteLine("The result is: " + finalResult);
	}
	public static void Part2(string fullEntries)
	{
		List<string> entries = fullEntries.Split('\n').ToList();
		Regex firstDigitPattern = new Regex("(one|two|three|four|five|six|seven|eight|nine|[0-9])");
		Regex lastDigitPattern = new Regex("(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])");
 
		var digitDict = new Dictionary<string, int>() {
			{ "one", 1 },
			{ "two", 2 },
			{ "three", 3 },
			{ "four", 4 },
			{ "five", 5 },
			{ "six", 6 },
			{ "seven", 7 },
			{ "eight", 8 },
			{ "nine", 9 },
			{ "eno", 1 },
			{ "owt", 2 },
			{ "eerht", 3 },
			{ "ruof", 4 },
			{ "evif", 5 },
			{ "xis", 6 },
			{ "neves", 7 },
			{ "thgie", 8 },
			{ "enin", 9 },
		};
		List<int> numbers = new List<int>();
		foreach (var entry in entries)
		{
			string first = firstDigitPattern.Match(entry).Groups[1].Value;
			
			var reversed = new string(entry.Reverse().ToArray());
			string last = lastDigitPattern.Match(reversed).Groups[1].Value;
			int firstParsed;
			bool firstWorked = int.TryParse(first, out firstParsed);
			if (!firstWorked)
			{
				firstParsed = digitDict[first];
			}
			int lastParsed;
			bool lastWorked = int.TryParse(last, out lastParsed);
			if (!lastWorked)
			{
				lastParsed = digitDict[last];
			}
			int result = int.Parse(string.Format("{0}{1}", firstParsed, lastParsed));
			numbers.Add(result);
		}
		
		int finalResult = numbers.Aggregate((a, b) => a + b);
		Console.WriteLine("The result is: " + finalResult);
	}
}