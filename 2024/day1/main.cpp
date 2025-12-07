
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>


std::vector<std::string> readFileLines(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::string> lines;
    std::string line;

    if (!file.is_open()) {
        // Handle error (file not found, etc.)
        return lines;
    }

    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    return lines;
}

int part1() {
	std::vector<std::string> pairs = readFileLines("input.txt");
	std::vector<int> left;
	std::vector<int> right;

	for (const std::string i : pairs) {
        std::istringstream iss(i);
        std::string part1, part2;
        iss >> part1 >> part2;
        left.push_back(std::stoi(part1));
        right.push_back(std::stoi(part2));
	}

	sort(right.begin(), right.end());
	sort(left.begin(), left.end());

	int diff = 0;

	for (int i = 0; i < left.size(); ++i) {
		diff += abs(left[i] - right[i]);
	};

	return diff;
}

int part2() {
	std::vector<std::string> pairs = readFileLines("input.txt");
	std::vector<int> left;
	std::map<int, int> right;

	for (const std::string i : pairs) {
    	std::istringstream iss(i);
    	std::string part1, part2;
    	iss >> part1 >> part2;
     	left.push_back(std::stoi(part1));
      	right[std::stoi(part2)]++;
	}

	int sum = 0;

	for (int i = 0; i < left.size(); ++i) {
		if (right.find(left[i]) != right.end()) {
			sum += left[i] * right[left[i]];
		}
	};

	return sum;
}

int main() {
	std::cout << "Part 1: " << part1() << std::endl;
	std::cout << "Part 2: " << part2() << std::endl;
	return 0;
}
