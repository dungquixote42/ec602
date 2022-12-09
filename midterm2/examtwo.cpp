// Copyright 2022 Hyunsoo Kim hkim42@bu.edu

#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::string;
using std::vector;

struct Team
{
    string name;
    char group;
    int matches_played = 0;
    int wins = 0;
    int draws = 0;
    int losses = 0;
    int goals_for = 0;
    int goals_against = 0;
    int goals_difference = 0;
    int points = 0;
    std::vector<char> last3 = {'x', 'x', 'x'};

    Team(string n, char g)
    {
        name = n;
        group = g;
    }
};

void print_for_group(std::vector<Team> teams, char g)
{
    cout << "Group " << g << "\n";
    cout << "Team                    MP W D L GF GA GD Pts     Last 3\n";
    for(Team t : teams)
    {
        if(t.group == g)
        {
            cout << t.name << "               ";
            cout << t.matches_played << " ";
            cout << t.wins << " ";
            cout << t.draws << " ";
            cout << t.losses << " ";
            cout << t.goals_for << " ";
            cout << t.goals_against << " ";
            cout << t.goals_difference << " ";
            cout << t.points << "     ";
            cout << t.last3[0] << " ";
            cout << t.last3[1] << " ";
            cout << t.last3[2] << "\n";
        }
    }
}

int main()
{
    std::cout << "entering main\n";

    int input;
    std::vector<Team> teams = {};
    while(1)
    {
        std::cout << "enter 0 to exit, 1 to add team, 2 to add match, 3 to print scoreboard\n";
        std::cin >> input;
        if(input == 0)
            break;
        else if(input == 1)
        {
            string n;
            char g;
            std::cout << "enter team name\n";
            std::cin >> n;
            std::cout << "enter group name\n";
            std::cin >> g;
            Team t(n, g);
            teams.push_back(t);
        }
        else if(input == 2)
        {
            string n1;
            int s1;
            std::cout << "enter team 1 name\n";
            std::cin >> n1;
            std::cout << "enter team 1 score\n";
            std::cin >> s1;

            string n2;
            int s2;
            std::cout << "enter team 2 name\n";
            std::cin >> n2;
            std::cout << "enter team 2 score\n";
            std::cin >> s2;

            for(int i = 0; i < teams.size(); ++i)
            {
                Team t = teams[i];
                if(t.name == n1)
                {
                    ++(t.matches_played);
                    t.last3[2] = t.last3[1];
                    t.last3[1] = t.last3[0];
                    if(s1 > s2)
                    {
                        ++(t.wins);
                        t.last3[0] = 'w';
                    }
                    else if(s2 > s1)
                    {
                        ++(t.losses);
                        t.last3[0] = 'l';
                    }
                    else
                    {
                        ++(t.draws);
                        t.last3[0] = 'd';
                    }
                    t.goals_for += s1;
                    t.goals_against += s2;
                    t.goals_difference = t.goals_for - t.goals_against;
                    t.points = 3*t.wins + t.draws;
                }
                if(t.name == n2)
                {
                    ++(t.matches_played);
                    t.last3[2] = t.last3[1];
                    t.last3[1] = t.last3[0];
                    if(s2 > s1)
                    {
                        ++(t.wins);
                        t.last3[0] = 'w';
                    }
                    else if(s1 > s2)
                    {
                        ++(t.losses);
                        t.last3[0] = 'l';
                    }
                    else
                    {
                        ++(t.draws);
                        t.last3[0] = 'd';
                    }
                    t.goals_for += s2;
                    t.goals_against += s1;
                    t.goals_difference = t.goals_for - t.goals_against;
                    t.points = 3*t.wins + t.draws;
                }
                teams[i] = t;
            }
        }
        else if(input == 3)
        {
            print_for_group(teams, 'A');
            print_for_group(teams, 'B');
            print_for_group(teams, 'C');
            print_for_group(teams, 'D');
            print_for_group(teams, 'E');
            print_for_group(teams, 'F');
            print_for_group(teams, 'G');
            print_for_group(teams, 'H');
        }
        else {}
    }

    std::cout << "exiting program\n";
}