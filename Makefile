build: 
	docker build -t django_test .
run:
	docker run -d -p 11010:8000 --name django_test django_test
stop:
	docker stop django_test