from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬的食譜資料庫
recipes = []

# 主頁面，顯示所有食譜
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

# 新增食譜頁面
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        sharer = request.form['sharer']
        content = request.form['content']
        
        # 儲存食譜資料
        recipes.append({
            'title': title,
            'sharer': sharer,
            'content': content
        })
        
        return redirect(url_for('index'))
    
    return render_template('add_recipe.html')

# 編輯食譜頁面
@app.route('/edit/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = recipes[recipe_id]
    
    if request.method == 'POST':
        # 更新食譜資料
        recipe['title'] = request.form['title']
        recipe['sharer'] = request.form['sharer']
        recipe['content'] = request.form['content']
        
        return redirect(url_for('index'))
    
    return render_template('edit_recipe.html', recipe=recipe, recipe_id=recipe_id)

# 刪除食譜
@app.route('/delete/<int:recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    # 根據 ID 刪除食譜
    recipes.pop(recipe_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)