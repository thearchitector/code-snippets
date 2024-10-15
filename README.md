# code snippets

1. create a minikube cluster
2. `helm repo add weaviate https://weaviate.github.io/weaviate-helm`
3. `helm install my-weaviate weaviate/weaviate --values weav.yaml`
4. `kubectl apply -f repl.yml`
5. `kubectl exec -it test -- bash`
6. run
  ```sh
  $ apt update && apt install vim -y
  $ pip install weaviate-client
  $ vim test.py
  # copy file contents
  $ python test.py
  created: 200
  returned: 100
```
