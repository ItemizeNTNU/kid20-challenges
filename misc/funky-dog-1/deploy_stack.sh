#!/bin/sh

if ! [ -x "$(command -v docker)" ]; then
  echo 'Unable to find docker command, please install Docker (https://www.docker.com/) and retry' >&2
  exit 1
fi

if ! [ -x "$(command -v faas-cli)" ]; then
  echo 'Unable to find faas-cli, installing now'
  curl -sSL https://cli.openfaas.com | sudo sh
fi

export BASIC_AUTH="true"
export AUTH_URL="http://basic-auth-plugin:8080/validate"
export OPENFAAS_URL="http://127.0.0.1:19999"

sha_cmd="shasum -a 256"
if ! command -v shasum >/dev/null; then
  sha_cmd="sha256sum"
fi

echo "Attempting to create credentials for gateway.."
echo "admin" | docker secret create basic-auth-user -
secret=$(head -c 16 /dev/urandom| $sha_cmd | cut -d " " -f 1)
echo "$secret" | docker secret create basic-auth-password -
if [ $? = 0 ];
then
  printf "[Credentials]\n username: admin \n password: $secret\n echo -n ""$secret"" | faas-cli login --username=admin --password-stdin"
else
  printf "[Credentials]\n already exist, not creating"
fi

echo ""
echo "Enabling basic authentication for gateway.."
echo ""

docker stack deploy func --compose-file "docker-compose.yml"

echo "Attempting to create flag.."
echo "KID20{4ll_my_c0d3_i5_fr0m_s74ck0v3rfl0w}" | docker secret create flag -

echo "Attempting to create secret-password.."
echo "wellILoveDogsNotGonnaLie" | docker secret create secret-password -

echo "Attempting to create secret-username.."
echo "KID20{w1th_5_l0ng_sp3c14l_u5s3rn4m3_n0b0dy_c5n_h4ck_m3}" | docker secret create secret-username -
