json_token=$(curl -k 'http://indian-banks-service.herokuapp.com/api/token/' \
-X POST -H 'Content-Type: application/json' \
-d '{"username":"archita77", "password":"archita77"}') && token=$(echo $json | sed "s/{.*\"token\":\"\([^\"]*\).*}/\1/g" | jq -r '.access')


# Get Access token from returned object in json_token
TOKEN=$(echo "$json_token" | jq -r '.access') 


echo -e "----------------------------------------------"
echo -e "Details of Bank with IFSC Code: UTBI0XAHM16"
echo -e "----------------------------------------------"
printf "\n"

curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" 'https://indian-banks-service.herokuapp.com/api/banks/UTBI0XAHM16'

printf "\n"
printf "\n"
echo -e "---------------------------------"
echo -e "Branches of YES Bank Ahmedabad"
echo -e "---------------------------------"

curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" 'https://indian-banks-service.herokuapp.com/api/branches?bank=yes-bank&city=ahmedabad&limit=3&offset=6'

printf "\n"
