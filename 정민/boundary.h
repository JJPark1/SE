#pragma once
#include <iostream>
#include <fstream>
#include "control.h"
using namespace std;

class JoinUI {
private:
	Join* join;
public:
	JoinUI(Join* j);
	void showMessage();
	void join_function();

};

class LoginUI {
private:
	Login* login;
public:
	LoginUI(Login* li);

};
class ResignUI
{
private:
	Resign* resign;
public:
	ResignUI(Resign* r);
	void showMessage();
};
class LogoutUI
{
private:
	Logout* logout;
public:
	LogoutUI(Logout* lo);
};