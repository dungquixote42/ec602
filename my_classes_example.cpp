#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::string;
using std::vector

// private vs public

// private : attribute is only accessible inside the class.

struct Course
{
    string name;
    string identifier;

    Course(string n, string i)
    {
        
    }
}

class Student
{
    public:
        int id_number;
        string name;
        vector<Course> Courses;

    Student() // __init__
    {
        cout << "made a student\n";
    }
    Student()(string s,  int myid)
    {
        id_number = myid;
        name = s;
    }

    void enroll() // add student to a course
    {

    }
};

int main()
{
    Student s;
    Student q("Messi", 37);
    std::cout << "VC Code Test\n";

    Student s;
    s.id_number = 123;

    return 0;
}