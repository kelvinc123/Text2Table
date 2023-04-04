DATA_PATH=$1
PRED_PATH=$2

export PYTHONPATH=.

printf "Wrong format:\n"
python scripts/eval/calc_data_wrong_format_ratio.py ${DATA_PATH} ${PRED_PATH} --row-header
for metric in E c BS-scaled; do
  printf "$metric metric:\n"
  python scripts/eval/calc_data_f_score.py ${DATA_PATH} ${PRED_PATH} --row-header --metric $metric
done