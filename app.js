function loadMoreNews() {
    const newsList = document.getElementById('news-list').querySelector('ul');
    const newNewsItem = document.createElement('li');
    newNewsItem.textContent = '새로운 공지사항: 학과 워크숍 안내';
    newsList.appendChild(newNewsItem);
}
