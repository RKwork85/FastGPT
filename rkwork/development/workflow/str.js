function getFinalDraft(translations) {
    // 分割字符串为数组，每轮翻译为一个元素
    const rounds = translations.split('\n\n');
    
    // 找到“定稿”的内容，它位于数组的倒数第二个元素
    const finalDraft = rounds[rounds.length - 2];
    
    // 返回“定稿”的内容
    return finalDraft.trim();
}

// 示例字符串
const translations = `第一轮：直译

愿年份平静，日子充满爱，手牵手直到老年。 

第二轮：优化

愿岁月静好，时光充满温情，相携之手直至暮年。 

第三轮：校验优化后的句子是否流畅

岁月静好，时光流转间爱意满满，携手同行，直至白头。 

第四轮：美化

愿时光轻柔，爱意如歌，你我手牵手，共赴岁月之巅。 

第五轮：定稿

岁月悠长，爱如歌谣，携手并肩，共度时光直至白首。`;

// 调用函数并打印结果
console.log(getFinalDraft(translations));