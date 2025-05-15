#include <iostream>
#include <ctime> // srand()

int rockPaperScissors()
{
    std::cout << "\n\n---------- ROCK PAPER SCISSORS! ----------\n\n";
    int inpRockPaperScissors;
    std::cout << "\t\n0: ROCK\t\n1: PAPER\t\n2: SCISSORS\n";
    std::cin >> inpRockPaperScissors;

    int randNum = rand() % 3;
    std::cout << "\tComputer chose: ";
    switch (randNum)
    {
    case 0:
        std::cout << "\n\tROCK\n";
        break;
    case 1:
        std::cout << "\n\tPAPER\n";
        break;
    case 2:
        std::cout << "\n\tSCISSORS\n";
        break;
    }

    if (inpRockPaperScissors < 0 || inpRockPaperScissors > 2)
        std::cout << "\t\nError: Invalid Input";
    else if (inpRockPaperScissors == randNum)
        std::cout << "\t\nTIE!";
    else if ((inpRockPaperScissors == 0 && randNum == 1) || (inpRockPaperScissors == 1 && randNum == 2) || (inpRockPaperScissors == 2 && randNum == 0))
        std::cout << "\t\nYOU LOSE!";
    else
        std::cout << "\t\nYOU WIN!";
    
    std::cout << "\t\n\nPlay again? (Y/N): ";
    char yn;
    std::cin >> yn;
    return (yn == 'y');
}

int main()
{
    srand(time(0));
    while (rockPaperScissors());
}