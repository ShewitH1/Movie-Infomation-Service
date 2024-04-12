from repositories.db import get_pool
from psycopg.rows import dict_row

def get_all_images_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                image_id,
                                caption,
                                created_at
                            FROM 
                                image
                            ''')
            return cursor.fetchall()
        

def get_image_bys_id(image_id):
    pool = get_pool()
    with pool.getconn() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                image_id,
                                caption,
                                created_at,
                                author_user,
                                image_link
                            FROM 
                                image
                            WHERE image_id = %s
                            ''', [image_id])
            return cursor.fetchall()
        

def create_image(caption, image_link, author_user):
    pool = get_pool()
    with pool.getconn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(''' 
                INSERT INTO image (caption, image_link, author_user)
                VALUES (%(caption)s, %(image_link)s, %(author_user)s)
                RETURNING image_id
                ;
            ''', {'caption': caption, 'image_link': image_link, 'author_user': author_user})
            res = cursor.fetchone()
            if not res:
                raise Exception('Failed to create movie')
            return res[0]