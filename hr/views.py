from time import sleep
import cv2
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import * 
webcam = cv2.VideoCapture(0)

# Create your views here.


def home(request):
    year = datetime.datetime.now().year
    dic = {}
    dic['year'] = year
    dic['name'] = 'rishabh'.upper()
    return render(request, 'hr/ask_actions.html', dic)


def results(request):
    dic = {}
    return render(request, 'hr/results.html', dic)


def gotoadduser(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/addnewprofile.html', dic)


def viewprofile(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/viewprofile.html', dic)


def editprofile(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/editprofile.html', dic)


def deleteprofile(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/deleteprofile.html', dic)


def attendancereport(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/attendancereport.html', dic)


def salary(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/salary.html', dic)


def editconfiguration(request):
    dic = {}
    year = datetime.datetime.now().year
    dic['year'] = year
    return render(request, 'hr/editconfiguration.html', dic)





def take_picture(request):
    while True:
        try:
            check, frame = webcam.read()
            print(check)  # prints true as long as the webcam is running
            print(frame)  # prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray, (28, 28))
                print("Resized...")
                img_resized = cv2.imwrite(
                    filename='saved_img-final.jpg', img=img_)
                print("Image saved!")

                break

            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
