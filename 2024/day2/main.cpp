#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

std::vector<std::vector<int>> readFileData(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::vector<int>> reports;
    std::vector<std::string> lines;
    std::string line;

    if (!file.is_open()) {
        throw std::invalid_argument("Err: No file with filename " + filename + " found!");
        return reports;
    }

    while (std::getline(file, line)) {
        if (line.empty()) continue;  // Skip empty lines

        std::stringstream iss(line);
        std::string s;
        std::vector<int> v;
        while (std::getline(iss, s, ' ')) {
            v.push_back(std::stoi(s));
        }

        reports.push_back(v);
    }
    return reports;
}

bool isSafe(const std::vector<int> rep) {
    // Originally the part 1 solution, changed to a function for ease of access for part 2

    std::string dir;

    if (rep[0] < rep[1]) {
        dir = "Up";
    } else if (rep[0] > rep[1]) {
        dir = "Down";
    } else {
        return false;
    }



    for (int i = 0; i < rep.size(); i++) {
        if (i + 1 >= rep.size()) { // Assume we're on the last level
            return true;
        }

        int diff = abs(rep[i] - rep[i + 1]);
        if (diff > 3 or diff == 0) break;

        if (dir == "Up" and rep[i] > rep[i + 1]) break;
        if (dir == "Down" and rep[i] < rep[i + 1]) break;
    }

    return false;
}


int part1(const std::vector<std::vector<int>> reports) {
    int safe = 0;

    for (const std::vector<int> rep : reports) {
        if (isSafe(rep)) safe++; // Logic moved to isSafe function
    }

    return safe;
}


int part2(const std::vector<std::vector<int>> reports) {
    int safe = 0;

    for (const std::vector<int> rep : reports) {
        if (isSafe(rep)) safe++;
        else {
            for (int i = 0; i < rep.size(); i++) {
                std::vector<int> modRep = rep;
                modRep.erase(modRep.begin() + i);
                if (isSafe(modRep)) {
                    safe++;
                    break;
                }
            }
        }
    }

    return safe;
}

int main() {
    std::vector<std::vector<int>> reports = readFileData("input.txt");
    std::cout << "Part 1: " << part1(reports) << std::endl;
    std::cout << "Part 2: " << part2(reports) << std::endl;
}
