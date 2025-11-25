#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
#include <list>

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
    std::list<int> column2;
    std::string word;
    while (file >> word) {
        column1.push_back(std::stoi(word));
        // std::cout<< *(--column1.end()) << "\n";
        file >> word;
        column2.push_back(std::stoi(word));
    }
    column1.sort();
    column2.sort();
    file.close();
    int sum = 0;
    std::list<int>::iterator it2 = column2.begin();
    for (std::list<int>::iterator it1 = column1.begin(); it1 != column1.end(); it1++) {
        
        sum += std::abs(*it2 - *it1);
        it2++;
    }
    std::cout << sum << "\n";
}