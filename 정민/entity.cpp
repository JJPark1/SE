#include <string>
#include "entity.h"


bool UserDetail::isValid(string name, string ssn, string id, string password)
{
    if (this->id == id && this->password == password)
    {


        return true;
    }
    else
        return false;
}
void UserDetail::addtoUser(string name,string ssn,string id,string password)
{// entitiy
    
    this->name = name;
    this->ssn = ssn;
    this->id = id;
    this->password = password;
}
void UserDetail::deletetoUser()
{
    name = "";
    ssn = "";
    id = "";
    password = "";
    cout << "resign complete" << endl;
}

void System::systemLogout()
{
    cout << "logout" << endl;
}

void System::removeAuthority()
{

}
