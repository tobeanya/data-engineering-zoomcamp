https://kestra.io/blogs/2024-04-05-getting-started-with-kestra


docker run --pull=always --rm -it -p 8080:8080 --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp kestra/kestra:latest server local

user: admin
last name: admin
password: RootRoot2025