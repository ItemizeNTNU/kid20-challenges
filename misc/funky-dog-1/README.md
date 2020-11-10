## Deployment

1.Initilize a docker swarm with:

```bash
docker swarm init
```

2.Run deploy_stack.sh script

3.Deploy functions:

```bash
# Login with secret created with deploy_stack.sh
echo -n XXXXXXXXXXXXXXXXXXX | faas-cli login --username=admin --password-stdin

faas build -f secret-vault.yml
faas deploy -f secret-vault.yml

cd functions/
faas build -f stack.yml
faas deploy -f stack.yml
```
