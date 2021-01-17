// live邮箱发送 可以用，但是邮件内容可能不是表专mime 

package main

import (
    "fmt"
    "net/smtp"
    "errors"
)


var host_smtp string  = "smtp-mail.outlook.com"
var host_port int = 587

var login_user string = "r32dfgg@live.com"
var password string = "ergreg"



type loginAuth struct {
    username, password string
}

func LoginAuth(username, password string) smtp.Auth {
    return &loginAuth{username, password}
}

func (a *loginAuth) Start(server *smtp.ServerInfo) (string, []byte, error) {
    return "LOGIN", []byte{}, nil
}

func (a *loginAuth) Next(fromServer []byte, more bool) ([]byte, error) {
    if more {
        switch string(fromServer) {
        case "Username:":
            return []byte(a.username), nil
        case "Password:":
            return []byte(a.password), nil
        default:
            return nil, errors.New("Unkown fromServer")
        }
    }
    return nil, nil
}


func mailSend(to, subject, text string) {
    msg := fmt.Sprintf(`To: %v
Subject: %v
From: <%v>
Content-Type: text/plain; charset=UTF-8

%v`, to, subject, login_user, text)
    fmt.Println(msg)
    auth := LoginAuth(login_user, password)
    hp := fmt.Sprintf("%v:%v", host_smtp, host_port)
    err := smtp.SendMail(hp, auth, login_user, []string{to}, []byte(msg))
    if err != nil {
        panic(err)
    }
}

func main() {
    mailSend("fwrefwe@gmail.com", "3243242ni什么22", "bvvt34r234hanzi汉字r")
}
