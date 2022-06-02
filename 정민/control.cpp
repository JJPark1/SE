#include <string>
#include "control.h"
#include "boundary.h"

void Join::requestJoin(string name,string ssn,string id,string password)
{ // 컨트롤
	UserDetail* userDetail;
	string n = name;
	string s = ssn;
	string i = id;
	string p = password;
	user->addUser(userDetail); // 유저 추가
	userDetail->addtoUser(n,s,i,p);
	joinUI->showMessage();


}
void Login::requestLogin()
{

}
void Logout::requestLogout()
{

}
void Resign::requestResign()
{

}