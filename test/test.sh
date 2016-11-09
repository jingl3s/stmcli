#!/bin/bash

# to grant bash is going to be used to run the script
# even if it's called like "sh test.sh"
if [ ! "$BASH_VERSION" ] ; then
    exec /bin/bash "$0" "$@"
fi

echo "data.check_for_update()"
echo "data.download_gtfs_data()"
echo "database.create_db()"
echo "database.init_table()"
echo "database.load_stm_data()"
echo "database.load_data()"
stmcli -y
if [[ $? -ne 0 ]]
then
  echo "Update Failed"
  exit 1
fi

echo "---------bus.next_departures()---------"
stmcli -s 51253 -b 435
if [[ $? -ne 0 ]]
then
  echo "bus.next_departures() Failed"
  exit 1
fi

echo "---------main() (custom time test)---------"
stmcli -s 51253 -b 435 -t 10:30
if [[ $? -ne 0 ]]
then
  echo "main() (custom time test) Failed"
  exit 1
fi

echo "---------bus.all_bus_for_stop_code()---------"
stmcli -s 51253
if [[ $? -ne 0 ]]
then
  echo "bus.all_bus_for_stop_code() Failed"
  exit 1
fi

echo "---------bus.all_bus_stop()---------"
stmcli -b 435
if [[ $? -ne 0 ]]
then
  echo "bus.all_bus_stop() Failed"
  exit 1
fi

echo "---------bus.metro_status()----------"
stmcli -m green
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi
stmcli -m orange
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi
stmcli -m yellow
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi
stmcli -m blue
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi
stmcli -m all
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi

echo "fr" > ~/.stmcli/lang.txt

stmcli -m all
if [[ $? -ne 0 ]]
then
  echo "bus.metro_status() Failed"
  exit 1
fi
echo "Not tested yet : data.date_in_scope()"
