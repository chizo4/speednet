# 🛜 `speednet`

> **Note**
This is a super quick personal tool to measure connection speed through the command line utilizing the [Speedtest interface](https://github.com/sivel/speedtest-cli/tree/master).

## Running the Code 🚀

Follow these steps to get `speednet` up and running on your machine:

1. **Check Python and Pip Installation:**
   Ensure you have `python3` and `pip` installed. You can verify their installation by running the following commands in your terminal:

   ```shell
   python3 -V
   pip -V
   ```

   > **Warning**
   If your shell fails to recognize these commands, please install Python and Pip from their official sites: [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/).

2. **Clone the Repository:**
   Clone the `speednet` repository from GitHub:

   ```shell
   git clone https://github.com/chizo4/speednet
   ```

3. **Setup:**
   Navigate to the root directory of the project and run the setup script:

   ```shell
   cd speednet
   bash setup.sh
   ```

4. **Define Aliases (optional but super useful):**
   You can define aliases in your shell configuration file (e.g., `.bashrc`, `.zshrc`). Add the following lines to your configuration file, adjusting the paths as necessary:

   ```shell
   alias speednet='python ~/{path}/speednet/code/main.py'
   alias speednet_down='python ~/{path}/speednet/code/main.py -t download'
   alias speednet_up='python ~/{path}/speednet/code/main.py -t upload'
   ```
  
   > **Note**
   Replace `{path}` with the actual path on your machine.
   After adding these lines, refresh your shell configuration by running `source ~/.bashrc` or `source ~/.zshrc`.

## Options and Usage 🛠️

`speednet` offers several options for testing your connection:

- **Full Connection Testing:**
  Run `speednet` without any arguments to perform both download and upload speed tests.
  ```shell
  python main.py
  ```

- **Download Testing Only:**
  To test only the download speed, use the `-t` option followed by either `download`, `down`, or `d` (case-insensitive).
  ```shell
  python main.py -t download
  ```

- **Upload Testing Only:**
  To test only the upload speed, use the `-t` option followed by either `upload`, `up`, or `u` (case-insensitive).
  ```shell
  python main.py -t upload
  ```

- **Help:**
  The `-h` option will display a help message detailing these options.
  ```shell
  python main.py -h
  ```

## Contribution & Collaboration 🤝

> **Note**
This is a very quick project with a small scope, but in case you had an idea on how to improve it, feel free to contact me via any of the links included in my [GitHub bio page](https://github.com/chizo4). Or, you might also contribute to the project by opening a [Pull Request](https://github.com/chizo4/speednet/pulls) with suggested improvements.
