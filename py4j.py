>>> import py4j
>>> from py4j.java_gateway import JavaGateway
>>> gateway = JavaGateway()                   # connect to the JVM
>>> py4j.java_gateway.launch_gateway(port=0, jarpath='', classpath='', javaopts=[], die_on_exit=False, redirect_stdout=None, redirect_stderr=None, daemonize_redirect=True, java_path='java', create_new_process_group=False, enable_auth=False, cwd=None, return_proc=False)
>>> random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
>>> number1 = random.nextInt(10)              # call the Random.nextInt method
>>> number2 = random.nextInt(10)
>>> print(number1, number2)
(2, 7)
>>> addition_app = gateway.entry_point               # get the AdditionApplication instance
>>> value = addition_app.addition(number1, number2) # call the addition method
>>> print(value)
9
