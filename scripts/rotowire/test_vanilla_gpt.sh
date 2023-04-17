DATA_PATH=$1
PRED_PATH=$2

export PYTHONPATH=.

for table in Team Player; do
  printf "$table table wrong format:\n"
  python scripts/eval/calc_data_wrong_format_ratio.py ${PRED_PATH} ${DATA_PATH} --row-header --col-header --table-name $table
  for metric in E c BS-scaled; do
    printf "Team table $metric metric:\n"
    python scripts/eval/calc_data_f_score.py ${PRED_PATH} ${DATA_PATH} --row-header --col-header --table-name $table --metric $metric
  done
done