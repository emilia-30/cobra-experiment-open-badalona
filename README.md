# Cobra trial experiment 
#### Badalona edition

---
 
### Installation
 
 1. Clone the repository from github
    ```sh
    git clone https://github.com/emilia-30/cobra-experiment-open-badalona.git    
    ```
 2. Move to project root
    ```sh
    cd cobra-experiment-open-badalona
    ```
 3. Install dependencies in both `/client` and `/server`
    ```sh
    pip install -r requirements.txt
    ```

---

### Running the experiment

1. to start the server, in `/server`:
    ```sh 
    python __main__.py
   ```


2. then start the 2 clients (eg in two new terminal windows), in `/client`:
    ```sh 
    python __main__.py
    ```

---

##### Notes

- developed using python v3.9.0 and other versions may not work
- to run on a network `host` should be changed in both `/server` and `/client` config files



## License
[MIT](https://choosealicense.com/licenses/mit/)