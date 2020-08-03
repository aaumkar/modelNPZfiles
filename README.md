# BE Final Year Project



<b>Summary:</b><br>
This repo shall contain `py` files to run the complete Program, function wise

## Read Files
`reading/read_files.py`

### Libraries used
|Name <br> Alphabetical | Usage | Dependance |
|-----------------------|-------|------------|
|numpy| export to `.npz`<br>| ###|
|pandas| Read and manage DataFrames<br> export to numpy| ###|
|os| get file names|###|
|tqdm| display progress on CLI | #|
<br>

| Function Name | Input | Ouput | Summary|
|---------------|-------|-------|----------------|--------|
| `get_labelled()`| `0 or 1`| `[filesnames]`| Read Files and return Files names labelled|
|`get_all()`|void| `[filenames]`| Get names of all 512 files|
|`get_path_labelled()`|`0 or 1`| path to labelled files | Get Path to labelled file names

