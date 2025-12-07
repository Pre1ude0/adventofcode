#include <regex>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

std::string readFileData(const std::string& filename) {
    std::ifstream file(filename);
    std::string content;

    if (!file.is_open()) {
        throw std::invalid_argument("Err: No file with filename " + filename + " found!");
        return content;
    }

    std::ostringstream ss;
    ss << file.rdbuf();
    content = ss.str();
    content.erase(std::remove(content.begin(), content.end(), '\n'), content.end());
    return content;
}

int part1(std::string data) {
    int result = 0;
    std::smatch m;
    std::regex e ("mul\\(\\d+?,\\d+?\\)");

    while (std::regex_search (data,m,e)) {
        for (std::string match:m) {
            match = match.substr(4, match.length() - 1); // Remove the `mul(` and `)`
            std::stringstream ss(match);
            std::string num;
            int pair[2];
            for (int i = 0; i < 2; i++) {
                std::getline(ss, num, ',');
                pair[i] = std::stoi(num);
            }
            result += pair[0] * pair[1];
        }

        data = m.suffix().str();
    }

    return result;
}

int part2(std::string data) {
    int result = 0;
    std::smatch m;

    std::regex d ("don't\\(\\).*?do\\(\\)");

    std::string data_copy = data;
    int curPos = 0;
    while (std::regex_search (data_copy,m,d)) {
        for (std::string match:m) {
            curPos = data.find(match) + match.length();
            data.replace(data.find(match), match.length(), std::string(match.length(), '#'));
        }
        data_copy = data.substr(curPos);
    }

    d = ("don't\\(\\).*");
    std::regex_search (data_copy,m,d);
    data.replace(data.find(m[0]), m[0].length(), std::string(m[0].length(), '#'));

    std::regex e ("mul\\(\\d+?,\\d+?\\)");

    while (std::regex_search (data,m,e)) {
        for (std::string match:m) {
            match = match.substr(4, match.length() - 1); // Remove the `mul(` and `)`
            std::stringstream ss(match);
            std::string num;
            int pair[2];
            for (int i = 0; i < 2; i++) {
                std::getline(ss, num, ',');
                pair[i] = std::stoi(num);
            }
            result += pair[0] * pair[1];
        }

        data = m.suffix().str();
    }

    return result;
}

int main() {
    std::string data = readFileData("input.txt");
    std::cout << "Part 1: " << part1(data) << std::endl;
    std::cout << "Part 2: " << part2(data) << std::endl;
    return 0;
}
