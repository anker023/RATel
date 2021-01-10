#ifndef OTHER_H
#define OTHER_H
#include <iostream>
using namespace  std;


string recvUltraSafe(int sock);  //Ensures that data is not corrupted and handles errors.
void sendUltraSafe(int sock, string data);
string generateToken(int length);


string exec(string command);
string getPath();
int changeDirectory(string path);

#endif