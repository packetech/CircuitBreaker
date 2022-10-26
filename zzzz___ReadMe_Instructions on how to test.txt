1. Download the three .py files and the zzz1_Test Results.txt file into a folder call it: circuitBreaker

2. Below are the Explanations and Instructions on how to test 

Explanation:
===========

When all services were working and the remote calls were returning without any errors, we call this state — “Closed”.

When the remote calls continued to fail and when we stopped making any more remote calls to the failing service, we call this state — “Open”

After a certain delay, when we make a remote call to the failing service, the state transitions from “Open” to “Half-Open”. If the remote call does not fail, then we transition the state from “Half Open” to “Closed” and the subsequent remote calls are allowed to be made. In case the remote call failed, we transition the state from “Half Open”, back to “Open” state and we wait for a certain period of time till we can make the next remote call (in Half Open state)


Instruction to test:
====================

1. In windows, Open PowerShell with Admin privilege
2. Do

pip install requests
pip install Flask
pip install ipython

3. Navigate to the folder containing our .py files (circuitBreaker)
4. run: setx FLASK_APP "main.py"
5. run: flask run 

These are to run our mock flask server

6. Open another PowerShell window, and navigate to our folder containing our .py files((circuitBreaker))
7. We assume python 3 installed already on your windows pc.  run: python


Now let's import our created libraries(note where our are getting the import from must have the same name as the .py):

8. from Circuit_Breaker import CircuitBreaker  
9. from testCode import make_request, faulty_endpoint, success_endpoint
10. breaker = CircuitBreaker(make_request, exceptions=(Exception,), error_threshold=3, time_window=20)
11. breaker.make_remote_call(success_endpoint)

See my success output result from the file "zzz1_Test Results.txt". you should get the same thing

And when we also try the faulty mock server:

12. breaker.make_remote_call(faulty_endpoint)

You should get an exception error, and if you try up to 3 times which is our error_threshold, it should finally OPEN the State and if you try any other, it will tell you to wait until the time_window or delay elapes

After our time_windows elapes, if your try the good server, it will bring the state of the breaker back to CLOSE, which allows flow of requests.

