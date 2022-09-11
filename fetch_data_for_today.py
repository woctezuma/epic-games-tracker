from pathlib import Path

from src.data_utils import load_sandbox_ids_dict
from src.fetch_utils import fetch_data_for_several_ids
from src.json_utils import save_json
from src.time_utils import get_fname_for_today


def main():
    output_fname = get_fname_for_today()
    Path(output_fname).parent.mkdir(parents=True, exist_ok=True)

    if not Path(output_fname).exists():
        sandbox_ids_dict = load_sandbox_ids_dict()
        data = fetch_data_for_several_ids(sandbox_ids=sandbox_ids_dict.values())
        save_json(data, output_fname)

    return


if __name__ == '__main__':
    main()
