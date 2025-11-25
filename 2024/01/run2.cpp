#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
#include <list>
#include <unordered_map>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        throw std::invalid_argument("Le seul argument doit etre l'entrée");
    }
    std::ifstream file;
    file.open(argv[1]);
    if (!file) {
        std::cerr << "Unable to open file datafile.txt\n";
        exit(1);
    }
    std::list<int> column1;
    std::unordered_map<int, int> column2;
    std::string word;
    while (file >> word) {
        column1.push_back(std::stoi(word));
        // std::cout<< *(--column1.end()) << "\n";
        file >> word;
        if (column2.find(std::stoi(word)) != column2.end()) {
            column2[std::stoi(word)]++;
        } else {
            column2[std::stoi(word)] = 1;
        }
    }
    file.close();
    int sum = 0;
    for (std::list<int>::iterator it1 = column1.begin(); it1 != column1.end(); it1++) {
        
        if (column2.find((*it1)) != column2.end()) {
            sum += *it1*column2[*it1];
        }
    }
    std::cout << sum << "\n";
}