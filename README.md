# Big Data Analytics – Homework #1  

### 📌 Overview  
This repository contains the implementation and documentation for **Homework #1** in the *Introduction to Big Data Analytics* course. The assignment covers:  
1. Installing and configuring **Apache Hadoop** on a **Windows** system.  
2. Performing **word count analysis** on *The Prince* by Niccolò Machiavelli using **Hadoop MapReduce** with **Python**.  
3. Enhancing analysis by **removing stopwords** and performing **bigram analysis**.  

All steps are designed to be reproducible on a local Windows environment using Hadoop 3.3.6 and Python 3+.

### ⚙️ Part 1: Install Hadoop on Your System

### 1. Install Java  
- Hadoop 3.3.x **requires JDK 8**.  
- Set `JAVA_HOME` environment variable:  
  ```cmd
  JAVA_HOME = C:\Program Files\Java\jdk1.8.0_XXX
  ```
- Add `%JAVA_HOME%\bin` to your system `PATH`.  
- Verify installation:
  ```cmd
  java -version
  ```

### 2. Install Hadoop  
- Download **Hadoop 3.3.6** from the [official Apache Hadoop releases page](https://hadoop.apache.org/releases.html).  
- Extract the `.tar.gz` file to:  
  ```
  C:\hadoop-3.3.6\hadoop-3.3.6\
  ```
- Set environment variable:
  ```cmd
  HADOOP_HOME = C:\hadoop-3.3.6\hadoop-3.3.6
  ```
- Add to `PATH`:  
  ```
  %HADOOP_HOME%\bin
  %HADOOP_HOME%\sbin
  ```

### 3. Configure Hadoop XML Files  
Edit files in `%HADOOP_HOME%\etc\hadoop\`:

#### `core-site.xml`
```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

#### `hdfs-site.xml`
First, create directories:
```
C:\hadoop-3.3.6\hadoop-3.3.6\data\namenode
C:\hadoop-3.3.6\hadoop-3.3.6\data\datanode
```
Then configure:
```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///C:/hadoop-3.3.6/hadoop-3.3.6/data/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///C:/hadoop-3.3.6/hadoop-3.3.6/data/datanode</value>
  </property>
</configuration>
```

#### `mapred-site.xml`
```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

#### `yarn-site.xml`
```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
```

#### `hadoop-env.cmd`
Update the Java path:
```cmd
set JAVA_HOME=C:\Program Files\Java\jdk1.8.0_XXX
```

### 4. Add `winutils.exe`  
- Download `winutils.exe` for Hadoop 3.3.6 ([GitHub – cdx/winutils](https://github.com/cdarlint/winutils)).  
- Place it in:  
  ```
  C:\hadoop-3.3.6\hadoop-3.3.6\bin\winutils.exe
  ```

### 5. Start Hadoop  
Run **Command Prompt as Administrator**:
```cmd
hdfs namenode -format
start-all.cmd
jps
```
You should see: `NameNode`, `DataNode`, `ResourceManager`, `NodeManager`.

---

## 🧪 Part 2: Word Count with Hadoop MapReduce

### 1. Data Preparation  
- Source: [*The Prince* by Niccolò Machiavelli](https://www.gutenberg.org/ebooks/1232) (Project Gutenberg).  
- Saved as: `C:\book-folder\book.txt`

### 2. Upload Data to HDFS
```cmd
hdfs dfs -mkdir /input
hdfs dfs -put C:\book-folder\book.txt /input/
```

### 3. Run Basic Word Count  
```cmd
hadoop jar %HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar ^
  -file C:\hadoop-scripts\mapper.py -mapper mapper.py ^
  -file C:\hadoop-scripts\reducer.py -reducer reducer.py ^
  -input /input/book.txt ^
  -output /output/wordcount
```

### 4. Results  
- **Total words**: 33,926  
- **Unique words**: 3,652  
- **Top words**: “the”, “and”, “to”

---

## 🔍 Part 3: Stopword Removal + Bigram Analysis

### 1. Stopword Removal  
Upload stopword list:
```cmd
hdfs dfs -put C:\hadoop-scripts\stopword_list.txt /input/
```

Run filtered word count:
```cmd
hadoop jar %HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar ^
  -file C:\hadoop-scripts\stopword_mapper.py -mapper stopword_mapper.py ^
  -file C:\hadoop-scripts\reducer.py -reducer reducer.py ^
  -file C:\hadoop-scripts\stopword_list.txt ^
  -input /input/book.txt ^
  -output /output/stopword_wc
```

**Results**:  
- **Total words**: 15,252  
- **Unique words**: 3,530  
- **Top meaningful words**: “prince”, “one”, “would”, “people”, “state”

### 2. Bigram Analysis  
Run bigram job:
```cmd
hadoop jar %HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar ^
  -file C:\hadoop-scripts\bigram_mapper.py -mapper bigram_mapper.py ^
  -file C:\hadoop-scripts\reducer.py -reducer reducer.py ^
  -file C:\hadoop-scripts\stopword_list.txt ^
  -input /input/book.txt ^
  -output /output/bigrams
```

**Top Bigrams**:  
- Content-relevant: `("prince", "must")`, `("new", "prince")`, `("every", "one")`  
- Metadata artifacts: `("project", "gutenberg")`, `("archive", "foundation")`

> ⚠️ **Note**: Future work should remove Project Gutenberg boilerplate for cleaner analysis.

---

## 💡 Additional Comments & Observations

- Hadoop on **Windows requires `winutils.exe`** and careful path handling—less stable than Linux/Docker setups.  
- The progression from raw word count → stopword filtering → bigrams demonstrates foundational **NLP preprocessing** in a distributed context.  
- For production or larger-scale experiments, consider migrating to **Linux**, **WSL**, or **cloud-based Hadoop (e.g., AWS EMR)**.

---

## 📚 References
- [Apache Hadoop Documentation](https://hadoop.apache.org/docs/)
- [Project Gutenberg – The Prince](https://www.gutenberg.org/ebooks/1232)
